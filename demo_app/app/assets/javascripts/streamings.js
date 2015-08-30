$( document ).ready(function() {
  $.slidebars();
  $('.button').on('click', function() {
    changeOrpheColor();
    scaling('green');
  });
});

function changeOrpheColor(){
  var url = "http://172.16.200.222:5000/estimote/beacon?color="+ $(this).val
  $.get(url, function( data ) {});
}


function scaling(color){
  $('#img').removeClass();
  $('#img').addClass(color);

  bigAnimation();

  function bigAnimation(){
    $('.' + color).animate({'scale': '1.3'},{
      duration: 210,
      complete: function(){
        smallAnimation();
      }
    });
  }

  function smallAnimation(){
    $('.' + color).animate({'scale': '1.1'},{
      duration: 210,
      complete: function(){
        bigAnimation();
      }
    });
  }
}


function shaking(){

  $('.now_shaking_box').show();

  $('.now_shaking').jrumble({
      rangeX: 0,
      rangeY: 0,
      rangeRot: 5,
      rumbleSpeed: 200,
  });

  var count = 0;
  var rumble = setInterval(function(){
    if( count % 2 == 0 ){
      $('.now_shaking').trigger('startRumble');
    }else{
      $('.now_shaking').trigger('stopRumble');
    }
    count++;
  },600);
  
}


//For test
function changeIndexState(color,motion){
  $.ajax({
    type: "POST",
    url: '/streamings/message',
    data: {
      "color": color,
      "motion": motion
    },
  });
}



//========================
// アニメーション スパーク
//========================
function spark() {

  var canvas = document.getElementById('canvas');
  if ( ! canvas || ! canvas.getContext ) { return false; }
  canvas.width = $(window).width();
  canvas.height = $(window).height();
  if( canvas.width > canvas.height ){
    var max = canvas.width;
  }else{
    var max = canvas.height;
  }
  var ctx = canvas.getContext('2d');

  var x = -100;
  var y = canvas.height / 2;
  var random_flg = Math.floor( Math.random() * 2 );
  var vy = Math.random() * 3;

  if( random_flg == 0 ){
    var y_flg = false; 
  }else{
    var y_flg = true; 
  }

  var animation = setInterval(function(){
    draw();
  },2);
  var count = 0;
  var particleMaster = [];


    function draw(){

    x += 10;
    if( ! y_flg ){
      y -= vy;
    }else{
      y += vy;
    }

    ctx.clearRect(0,0,canvas.width,canvas.height);
    // ctx.beginPath();
    // ctx.fillStyle = 'rgba(0,0,0,0.1)';
    // ctx.fillRect(0,0,canvas.width,canvas.height);

    // var img = new Image();
    // ctx.globalAlpha = 0.2;
    // img.src = "img/" + color + ".png";
    // ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

    ctx.beginPath();
    ctx.strokeStyle = 'none';
    ctx.fillStyle = '#ffffff';
    ctx.arc(x, y, 10, 0, 2*Math.PI, false);
    ctx.globalAlpha = 1;
      ctx.fill();

      
      particleMaster[count] = new particle(x,y,ctx);  
      for( var i = 0; i <= count; i++){
        particleMaster[i].draw();
      }

      if( x > canvas.width*4 ){
        clearInterval(animation);
      }

    count++;
    }
   
}


function particle(start_x,start_y,ctx){

  var x = start_x;
  var y = start_y;
  var size = Math.floor( Math.random() * 8 ) + 4;
  var count = 0;
      
    this.draw = function(){

      if( count <= 100 ){
        x += Math.floor( Math.random() * 12 ) - 6;
        y += Math.floor( Math.random() * 18 ) - 9;
        var plus_random_x = Math.floor( Math.random() * 60 ) - 30;
      var plus_random_y = Math.floor( Math.random() * 60 ) - 30;
      ctx.beginPath();
      if( count <= 25 ){
        ctx.fillStyle = '#ffffff';
      }else if( count > 40 && count <= 60 ){
        ctx.fillStyle = 'rgba(255,255,255,0.6)';
      }else if( count > 60 && count <= 80 ){
        ctx.fillStyle = 'rgba(255,255,255,0.4)';
      }else if( count > 80 ){
        ctx.fillStyle = 'rgba(255,255,255,0.2)';
      }
      ctx.arc(x, y, size, 0, 2*Math.PI, false);
      ctx.arc(x+plus_random_x, y+plus_random_y, size, 0, 2*Math.PI, false);
        ctx.fill();
        count++;
    }
    }
}



//========================
// アニメーション 花火
//========================
function hanabi() {

  var canvas = document.getElementById('canvas');
  if ( ! canvas || ! canvas.getContext ) { return false; }
  canvas.width = $(window).width();
  canvas.height = $(window).height();
  if( canvas.width > canvas.height ){
    var max = canvas.width;
  }else{
    var max = canvas.height;
  }
  var ctx = canvas.getContext('2d');

  var center_x = canvas.width / 2;
  var center_y = canvas.height / 2;
  var x = center_x;
  var y = center_y;
  var xs = center_x;
  var ys = center_y;
  var vx = 0;
  var vy = 0; 
  var particle_count = 36;
  var radius = 0;
  var rad = 0;
  var degree = 50;
  rad = degree * Math.PI / 180;
  var count = 0;


  var animation = setInterval(function(){
    draw();   
  },10);


  function draw(){

    vx += Math.floor( Math.random() * 20 ) - 10;
    vy += Math.floor( Math.random() * 20 ) - 10;

    x += vx;
    y += vy;

    ctx.clearRect(0,0,canvas.width,canvas.height);
    // ctx.beginPath();
    // ctx.fillStyle = 'rgba(0,0,0,0.6)';
    // ctx.fillRect(0,0,canvas.width,canvas.height);

    // var img = new Image();
    // ctx.globalAlpha = 0.6;
    // img.src = "img/" + color + ".png";
    // ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

    radius += 10;

    for( var i = 0; i <= particle_count; i++){
      degree = i * (360 / particle_count);
      rad = degree * Math.PI / 180;
      random_radius = Math.floor( Math.random() * 20 ) - 10;
      x = Math.sin(rad) * radius + center_x;
      y = Math.cos(rad) * radius + center_y;

      ctx.beginPath();
      ctx.strokeStyle = 'none';
      ctx.fillStyle = '#ffffff';
      ctx.arc(x, y, 12, 0, 2*Math.PI, false);
      ctx.fill();
    }

    if( count >= 20 ){
      for( var i = 0; i <= 20; i++){
        degree = i * (360 / 20);
        rad = degree * Math.PI / 180;
        xs = Math.sin(rad) * (radius - 200) + center_x;
        ys = Math.cos(rad) * (radius - 200) + center_y;

        ctx.beginPath();
        ctx.strokeStyle = 'none';
        ctx.fillStyle = '#ffffff';
        ctx.arc(xs, ys, 8, 0, 2*Math.PI, false);
        ctx.fill();
      } 
    }

    if( radius + 200 > max + 300){
      clearInterval(animation);
    }

    count++;  

  }

}




//========================
// アニメーション bubble
//========================
function bubble(){

  var canvas = document.getElementById('canvas');
  if ( ! canvas || ! canvas.getContext ) { return false; }
  canvas.width = $(window).width();
  canvas.height = $(window).height();
  if( canvas.width > canvas.height ){
    var max = canvas.width;
  }else{
    var max = canvas.height;
  }
  var ctx = canvas.getContext('2d');

  var flower_particle = [];
  var particle_count = 200;
  var count = 0;


  for(var i = 0; i <= particle_count; i++){
    flower_particle[i] = new bubbleLoop(canvas,ctx);
  }

  var animation = setInterval(function(){
    if( count < 100 ){
      ctx.clearRect(0,0,canvas.width,canvas.height);
      ctx.beginPath();
      // ctx.fillStyle = 'rgba(0,0,0,0.2)';
      // ctx.fillRect(0,0,canvas.width,canvas.height);

      // var img = new Image();
      // ctx.globalAlpha = 0.5;
      // img.src = "img/" + color + ".png";
      // ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      for(var i = 0; i <= particle_count; i++){
        flower_particle[i].draw();
      }
      count++;
    }else{
      clearInterval(animation);
    }
  },10);

}


function bubbleLoop(canvas,ctx) {

  var center_x = canvas.width / 2;
  var center_y = canvas.height / 2;
  var x = center_x;
  var y = center_y;
  var vx = 0;
  var vy = 0; 
  var topspeed = 10;
  var radius = 1;
  var rad = 0;
  var degree = 0;
  var size = Math.floor( Math.random() * 15 );
  var anime_count = 0;
  var delete_count = Math.floor( Math.random() * 40 ) + 40;

  rad = degree * Math.PI / 180;
  var count = 0;


  this.draw = function(){

    vx += ( Math.random() * 6 ) - 3;
    vy += ( Math.random() * 6 ) - 3;
    limit(topspeed);
    x += vx;
    y += vy;

    function limit(maxspeed){
      if( vx > maxspeed){
        vx = maxspeed;
      }
      if( vy > maxspeed){
        vy = maxspeed;
      }
    }

    if( anime_count < delete_count ){
      ctx.beginPath();
      ctx.strokeStyle = 'none';
      ctx.fillStyle = '#ffffff';
      ctx.arc(x, y, size, 0, 2*Math.PI, false);
      ctx.fill();
    }

    anime_count++;

  }

}




