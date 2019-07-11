Title: How To Hide Some Field in Django Queryset
Slug: how-to-hide-some-field-in-django-queryset
Date: 2019-07-19 10:45
Tags: python, django, values, hide fields, hide relationship
Category: Django
Summary: The original problem is, how to not select particular field when do a query in Django model? There're some approach to handle this problem. I'll show you three approaches to handle this. Keep Reading, and give your thoughts.

# Bismillah

## Introduction
When work with user permission, sometimes we need to hide some field for particular user not other. In Django, you can use approaches that I will mention here in this article.

The objectives of this article are:

1. Problem Definition
2. Approaches to handle this problem.

Lets dive into the problem definition or the user story.

## 1. Problem Definition

### User Story

A teacher can create a quiz, write description, and questions for that quiz. But, Don't display the questions into student that not registered into that quiz. 
Only teacher who create the quiz, and registered user can see the questions of the quiz. Plus: the quiz will expired after 10 days.

### Break Down

So, there are some points:

1. Teacher User create quiz
2. Quiz detail view, only these users can see the questions:
    - Teacher who created the quiz
    - Students who registered to that quiz
3. Quiz expiration

In this article, we will only focus on the second point. We will make assumptions for the first point and third point in the section below.

### Assumptions

#### The model

We have 2 user model, Teacher and Student. Then another two model for Quiz and Question. For simplicity, we will define these simple models in our models.py

```
from django.db import models


class Teacher(models.Model):
    name = models.CharField()


class Student(models.Model):
    name = models.CharField()


class Quiz(models.Model):
    title = models.CharField()
    description = models.TextField()
    created_by = models.ForeignKey(Teacher)
    students = models.ManyToMany(Student)
    _is_expired = models.BooleanField(verbose_name='is_expired', default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    @property
    def is_expired(self):
        if self._is_expired:
            return True
        
        # some logic to check expiration, and update the _is_expired to True if expired
        return is_expired # assumed that is_expired defined


class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz)
```

#### What Is is_expired property

It's to prevent django do make calculation when the quiz already expired.

### 2. Approaches

There are some approaches, to handle hiding values to achieve our problem here.
In this article, we will talk about three approaches. I'll try to cover how-to, some short explanation if required and the plus-minus for each approach.

Lets dive in...

#### 1. Let developer decide the permission in the template

Okay, Its a simple approach. Make a query for a quiz, and pass it into the template's context. Then, let developer to decide what fields of quiz will displayed into a user, and not displayed in the template.

Let's look at the implementation:

```
# views.py

def detail_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    return render_template(request, templatename, {'quiz': quix})

# in template

{# to show questions #}

{% if request.user == quiz.created_by or request.user in quiz.students.all() %}

{% for question in quiz.questions.all() %}
    {# show the questions %}
{% endfor %}
{% else %}
Only Registered user can see the questions
{% endif %}


```

This can be done in Django because of the django's reverse relationship.

**The Pros**:

- Simple view, yes we only do query for quiz

**The Cons**:

- Decision logic at your template. This is not intended to be placed in the template. The template is only place for representational purpose.
- When developer forgot to filter user, all user can see all questions.


#### 2. Disable reverse relations

Okay, back to the model, at Question model we change to:

```
class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, related_name='+')
```

when we use `related_name='+'` in the `ForeignKey` we disable reverse relation. With that in our mind, we can't do query like this `quiz.questions.all()`.

So, how we can decide user that has permission to see questions and not?

```
def detail_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)

    context = {
        'quiz': quiz
    }

    allowed_see_questions = any([
        request.user == quiz.created_by,
        request.user in quiz.students.all()
    ])

    if allowed_see_questions:
        context['questions'] = Question.objects.filter(quiz=quiz)

    return render_template(request, templatename, context)

```

You can see, we pass `questions` as context when user is allowed to see questions. If not, we not pass anything about questions. And in template, we only make test: `if questions`.

**The Pros**

- this is the place for things like that. As view in django is a controller.
- no permission checking in the template

**The Cons**
- yes, more code in view / controller

#### 3. use values in queryset

Another way is to use `values` in the queryset. It's called like `Quiz.objects.values('description').all()`. Its will return queryset with dictionary object with key described in the `values` params for each item. It's just like `SELECT a, b, c FROM x` in the SQL query.

This is best way to do for the most field permissions. But, in our case, we want to access `is_expired` property in the quiz object. So, we can't do `values` at this problem.


## At The End

Yes, I think there are more and more approaches to handle situation like this. If you have any, you can contribute to me in the comment below. And we can share our decission to help other developers if they have problem like this.

So, That is 3 approaces to problem like I described before. And thanks for your time and reading..

