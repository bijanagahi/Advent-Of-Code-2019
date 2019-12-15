
let puzzle_input = `<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>`

let NUM_STEPS = 1000;
let SCALE = 1;
let moons = []
let permutations;
let currentStep = 0;

function setup() {
  createCanvas(600, 600,WEBGL);
  frameRate(5)
  var iter = 0;
  for( var l of puzzle_input.split('\n')){
    m = new Moon(l,iter++);
    moons.push(m);
    console.log(m.toString());
  }
  console.log('--------------');
  permutations = getPermutations(moons, 2);
  iter = 0;
  for(var p of permutations){
     if (p[0].id == p[1].id){
      permutations.splice(iter,1); 
     }
    iter ++
  }
  // console.log(permutations);
}

function draw() {
  scale(10)
  // for (var x = 1;x<=NUM_STEPS;x++){
    currentStep++;
    if (currentStep %500 ==0){
       console.log("On step:"+currentStep); 
    }
    background(220);
    for(var p of permutations){
      p[0].calculateGravity(p[1]);
    }
    for (var moon of moons){
      moon.update()
      moon.draw()
      // console.log(moon.toString())
    }

    
    if( currentStep >= NUM_STEPS){
      console.log("Done.")
      noLoop()
    }
  // }

}