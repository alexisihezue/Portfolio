## rules
# use the left/right arrows to align the bunny, press the space button to jump, and hit the box that corresponds to the color WRITTEN on the screen before the timer runs out

var back = createSprite(200,200);
back.setAnimation("sky");

var red = createSprite(50,210);
red.setAnimation("red");
red.scale = 0.12;
red.setCollider("rectangle");

var blue = createSprite(150,210);
blue.setAnimation("blue");
blue.scale = 0.025;
blue.setCollider("rectangle");

var green = createSprite(250,210);
green.setAnimation("green");
green.scale = 0.0258;
green.setCollider("rectangle");

var yellow = createSprite(350,210);
yellow.setAnimation("yellow");
yellow.scale = 0.245;
yellow.setCollider("rectangle");

var bunny = createSprite(50,323);
bunny.setAnimation("bunny");
bunny.scale = 0.3;
bunny.setCollider("rectangle");



var a = randomNumber(35,358);
var b = randomNumber(150,10); 

var timer = 0;
var balloon = Math.round(randomNumber(1,16));


var score = 0;
var r = "Red";
var bl = "Blue";
var g = "Green";
var y = "Yellow";

function bounce() {
 timer = timer + 1;
  if (timer == 105) {
    a = randomNumber(35,358);
    b = randomNumber(150,10);
    balloon = Math.round(randomNumber(1,16));
  } if (timer > 105) {
    timer = 0;
  }
}
function resetPosition() {
  bunny.y = 323;
}

//functions for algorithm/reset

function resetFinalposition() {
  bunny. y = 323; 
  bunny.x = 50; 
}
function resetScore() {
  score = 0; 
}

function lowerScore() {
  score = score - 500; 
}


World.frameRate        = 1000;

function draw() {
  if (score==-500) {
    resetFinalposition();
    resetScore();
  }
  bounce();
  if (bunny.y > 323) {
    bunny.y = 323;
  }
  if (bunny.y < 200) {
    bunny.y = 323; 
  }
  if (bunny.x < 0) {
    bunny.x = 378;
  }
  if (bunny.x > 400) {
    bunny. x = 10; 
  }
  if (keyWentDown("space")) { 
    bunny.velocityY = -2;
    bunny.setAnimation("bunny");
  }
  if (keyWentUp("space")) { 
    bunny.velocityY = 0;
    bunny.setAnimation("bunny");
  }
  if (keyDown("right")) {
    bunny.x = bunny.x + 3; 
    bunny.setAnimation("bunnyr");
  } else {
    bunny.velocityX = 0; 
  }
  if (keyDown("left")) {
    bunny.x = bunny.x - 3;
    bunny.setAnimation("bunnyl");
  } else {
    bunny.velocityX = 0;
  }
  if (keyWentUp("right")) { 
    bunny.setAnimation("bunny");
  }
  if (keyWentUp("left")) { 
    bunny.setAnimation("bunny");
  }
  if (keyDown("down")) {
    bunny.y = bunny.y + 10;
    bunny.setAnimation("bunny");
  } else {
    bunny.velocityX = 0;
  }
  
  if (keyWentUp("down")) { 
    bunny.setAnimation("bunny");
  }
  if ((bunny.isTouching(red)) && ((balloon == 1))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  } 
  if ((bunny.isTouching(green)) && ((balloon == 1))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 1))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 1))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 8))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 8))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 8))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 8))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 9))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 9))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 9))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 9))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 10))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 10))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 10))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 10))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 2))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 2))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 2))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 2))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 5))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 5))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 5))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 5))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 6))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 6))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 6))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 6))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 7))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 7))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 7))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 7))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 4))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 4))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 4))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 4))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 14))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 14))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 14))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 14))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 15))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 15))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 15))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 15))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 16))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 16))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 16))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 16))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 3))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 3))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 3))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 3))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 11))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 11))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 11))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 11))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(green)) && ((balloon == 12))) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 12))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 12))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 12))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if (bunny.isTouching(green) && balloon == 13) { 
    score = score + 500;
    resetPosition();
    bounce(); 
  }
  if ((bunny.isTouching(red)) && ((balloon == 13))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(yellow)) && ((balloon == 13))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  if ((bunny.collide(blue)) && ((balloon == 13))) { 
    lowerScore();
    resetPosition();
    bounce(); 
  }
  drawSprites();

  if (balloon == 1) { 
  fill("red");
  textSize(20);
  text(r, a, b, 20, 20);
  }
  if (balloon == 2) { 
  fill("blue");
  textSize(20);
  text(bl, a, b, 20, 20);
  }
  if (balloon == 3) { 
  fill("green");
  textSize(20);
  text(g, a, b, 20, 20);
  }
  if (balloon == 4) { 
  fill("yellow");
  textSize(20);
  text(y,a, b, 20, 20);
  }
  if (balloon == 5) { 
  fill("yellow");
  textSize(20);
  text(bl,a, b, 20, 20);
  }
  if (balloon == 6) { 
  fill("green");
  textSize(20);
  text(bl,a, b, 20, 20);
  }
  if (balloon == 7) { 
  fill("red");
  textSize(20);
  text(bl,a, b, 20, 20);
  }
  if (balloon == 8) { 
  fill("yellow");
  textSize(20);
  text(r,a, b, 20, 20);
  }
  if (balloon == 9) { 
  fill("blue");
  textSize(20);
  text(r,a, b, 20, 20);
  }
  if (balloon == 10) { 
  fill("green");
  textSize(20);
  text(r,a, b, 20, 20);
  }
  if (balloon == 11) { 
  fill("yellow");
  textSize(20);
  text(g,a, b, 20, 20);
  }
  if (balloon == 12) { 
  fill("red");
  textSize(20);
  text(g,a, b, 20, 20);
  }
  if (balloon == 13) { 
  fill("blue");
  textSize(20);
  text(g,a, b, 20, 20);
  }
  if (balloon == 14) { 
  fill("green");
  textSize(20);
  text(y,a, b, 20, 20);
  }
  if (balloon == 15) { 
  fill("red");
  textSize(20);
  text(y,a, b, 20, 20);
  }
  if (balloon == 16) { 
  fill("blue");
  textSize(20);
  text(y,a, b, 20, 20);
  }
  
  fill("black");
  textSize(20);
  text("Score: ", 226, 368, 20, 20);
  text(score, 301,368,20,20);
  
  fill("black");
  textSize(20);
  text("Timer: ", 49, 158, 20, 20);
  text(timer, 110,158,20,20);
}
