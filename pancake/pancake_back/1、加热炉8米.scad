//炉体
module luti() {
     difference(){
        translate([0,0,0])
            cube([8000,450,450],true);
       translate([0,0,0])
            cube([8000,370,370],true);

     }
}
translate([0,0,790])luti();

//支架
module zhijia(){
     color("blue")translate([0,235,600])
         cube([9000,40,40],true);
     color("blue")translate([0,-235,600])
         cube([9000,40,40],true);        
}
zhijia();

//支腿
module zhitui(){
    color("blue")translate([0,235,290])rotate([0,90,0]) 
        cube([580,40,40],true);  
    color("blue")translate([0,-235,290])rotate([0,90,0]) 
        cube([580,40,40],true);             
}
//zhitui();

function f(x) = 0.5 * x ;
color("blue")
    for (a = [ -4500 : 600 : 4500 ])
//        translate([a, f(a), 0]) cube(2, center = true);
        translate([a, 0, 0])zhitui() ;
    
     
//模具
module muju(){
     color("steelblue")translate([0,0,0])rotate([0,0,90]) 
           cylinder(250,150,150, center=true);
}   
function f(x) = 0.5 * x ;
color("blue")
    for (a = [ -4500 : 300 : 4500 ])
//        translate([a, f(a), 0]) cube(2, center = true);
        translate([a, 0, 805])muju() ;
    
//拖棍
module tuogun(){
     color("steelblue")translate([0,20,0])rotate([90,0,0]) 
           cylinder(550,15,15, center=true);
     color("steelblue")translate([0,0,0])rotate([90,0,0]) 
           cylinder(300,30,30, center=true);
}
//tuogun();

//链轮
module lianlun(){
     color("blue")translate([0,270,0])rotate([90,0,0]) 
           cylinder(8,40,40, center=true);
     color("blue")translate([0,290,0])rotate([90,0,0]) 
           cylinder(8,40,40, center=true);
}
//lianlun();

//轴承ucp30
module ucp30(){
     color("blue")translate([0,0,0])rotate([90,0,0]) 
         cylinder(30,25,25, center=true);
     color("blue")translate([0,0,-25])rotate([0,0,0]) 
         cube([100,40,15],true);
}

//拖棍组
module tuogunzu(){
    union(){
        translate([0,0,650]){
            tuogun();
            lianlun();
            translate([0,235,0])ucp30();
            translate([0,-235,0])ucp30();
         }
    }
}
//tuogunzu();

echo(version=version());

function f(x) = 0.5 * x ;

color("blue")
    for (a = [ -4500 : 120 : 4500 ])
        translate([a, 0, 0])tuogunzu() ;

//加热风口
module fengkou(){
     color("blue")translate([0,-235,600])
         cube([600,400,100],true);
     
}
fengkou();
 