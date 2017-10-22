var keyData = {
    a:{
        color: "indianred",
        sound: var Howl({
            src: ['sounds/Bear growl.wav']
        })
    },
    s:{
        color: "salmon",
        sound: var Howl({
            src: ['sounds/Bee buzzing.wav']
        })
    },
    d:{
        color: "crismon",
        sound: var Howl({
            src: ['sounds/Bird chirp Mexican Red Parot.wav']
        })
    },
    f:{
        color: "deeppink",
        sound: var Howl({
            src: ['sounds/Bird song.wav']
        })
    },
    g:{
        color: "coral",
        sound: var Howl({
            src: ['sounds/Bird songs.wav']
        })
    },
    h:{
        color: "tomato",
        sound: var Howl({
            src: ['sounds/Canary.wav']
        })
    },
    j:{
        color: "orange",
        sound: var Howl({
            src: ['sounds/Canary trills 1.wav']
        })
    },
    k:{
        color: "khaki",
        sound: var Howl({
            src: ['sounds/Cat meow 1.wav']
        })
    },
    l:{
        color: "lavender",
        sound: var Howl({
            src: ['sounds/Cat meow 2.wav']
        })
    },
    z:{
        color: "violet",
        sound: var Howl({
            src: ['sounds/Cat meow 4.wav']
        })
    },
    x:{
        color: "fuchsia",
        sound: var Howl({
            src: ['sounds/Chicken coop.wav']
        })
    },
    c:{
        color: "purple",
        sound: var Howl({
            src: ['sounds/Chickens.wav']
        })
    },
    v:{
        color: "slateblue",
        sound: var Howl({
            src: ['sounds/Crickets.wav']
        })
    },
    b:{
        color: "magenta",
        sound: var Howl({
            src: ['sounds/Duck quacking 1.wav']
        })
    },
    n:{
        color: "red",
        sound: var Howl({
            src: ['sounds/Duck quacking 2.wav']
        })
    },
    m:{
        color: "palegreen",
        sound: var Howl({
            src: ['sounds/Elephant.wav']
        })
    },
    q:{
        color: "blue",
        sound: var Howl({
            src: ['sounds/Elephant trumpeting.wav']
        })
    },
    w:{
        color: "green",
        sound: var Howl({
            src: ['sounds/Finch.wav']
        })
    },
    r:{
        color: "olivedrab",
        sound: var Howl({
            src: ['sounds/Geese Canadian flock.wav']
        })
    },
    t:{
        color: "lightseagreen",
        sound: var Howl({
            src: ['sounds/Herd sheep.wav']
        })
    },
    y:{
        color: "yellow",
        sound: var Howl({
            src: ['sounds/Horses walking on dirt.wav']
        })
    },
    u:{
        color: "cyan",
        sound: var Howl({
            src: ['sounds/Mosquito.wav']
        })
    },
    i:{
        color: "maroon",
        sound: var Howl({
            src: ['sounds/Owl.wav']
        })
    },
    o:{
        color: "peru",
        sound: var Howl({
            src: ['sounds/Parrot.wav']
        })
    },
    p:{
        color: "tan",
        sound: var Howl({
            src: ['sounds/Vulture 1.wav']
        })
    }
}

var circles = [];

function onKeyDown(event){
    if(keyData[event.key]){
        var randomPoint = Point.random() * view.size;
        var circle = new Path.Circle(randomPoint, 300);
        circles.push(circle);
        circle.fillColor = keyData[event.key].color;
    }
}
