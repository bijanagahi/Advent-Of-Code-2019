class Moon {
  constructor(line, mid) {
    this.pos = this.parseInput(line);
    this.vel = [0,0,0];
    this.id = mid;
    this.color = [random(0,255),random(0,255),random(0,255)]
  }
  
  parseInput(i) {
    var re = /(-?\d{1,})/g;
    var matches = [...i.matchAll(re)];
    if(matches.length != 3){
      console.log("regex parse error");
      return;
    }
    return [
      parseInt(matches[0][0]),
      parseInt(matches[1][0]),
      parseInt(matches[2][0])
    ]
  }
  
  calculateGravity(adj){
    // var i = 0;
    // console.log('ADJ:'+adj.toString())
    for(var i = 0;i<3;i++){
      // console.log("Comparing "+this.pos[i]+" and "+adj.pos[i])
      if (this.pos[i] == adj.pos[i])
        continue;
      this.vel[i] += (this.pos[i] < adj.pos[i]) ? 1:-1
    }
    // console.log("New Vel: "+this.vel)
  }
  
  update(){
    for (var i=0;i<3;i++){
      this.pos[i] += this.vel[i]
    }
  }
  
  draw(){
    push()
    translate(this.pos[0]*SCALE,this.pos[1]*SCALE,this.pos[2]*SCALE)
    noStroke()
    fill(this.color);
    sphere(1)
    pop()
  }
}

Moon.prototype.toString = function s() {
  return '' + this.id+' | '+this.pos+' | '+this.vel;
}