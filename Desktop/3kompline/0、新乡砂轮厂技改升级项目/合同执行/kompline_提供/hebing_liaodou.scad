use</Users/wlniu/Desktop/OpenSCAD.app/Contents/Resources/examples/Advanced/children.scad>
use</Users/wlniu/Desktop/OpenSCAD.app/Contents/Resources/examples/Basics/CSG-modules.scad>
use</Users/wlniu/Desktop/OpenSCAD.app/Contents/Resources/examples/Basics/Linear_extrude.scad>
use</Users/wlniu/Desktop/OpenSCAD.app/Contents/Resources/Examples/Functions/polygon_areas.scad>

use </Users/wlniu/kompline/pancake/pidaizhao.scad>
use </Users/wlniu/kompline/pancake/robot.scad>
use </Users/wlniu/kompline/tuiretie/tuiretie.scad>


//称量料斗
module ld(){
color("green")
    translate([0, 0, 0])
        linear_extrude(height = 300, scale = 150)
            circle([1], center = true);
}
//传感器
module chuanganqi(){
    union(){
        difference(){
           cube([130,24,22],center= true);{
               for (a = [-56.5:113:56.5])translate([a,0,0]){
                    for (b = [-7.5:15:7.5])translate([0,b,0])scale([0.6,0.6,1.5])holeC();
        }
        }
    }
       for (a = [-56.5:113:56.5])translate([a,0,0]){
         for (b = [-7.5:15:7.5])translate([0,b,-15]) loushuan();
         }
}
}
//translate([150,0,40])chuanganqi();
//loushuan();
//连接件
module lianjiejian(){
    color("lime"){translate([95,0,54])cube([40,50,5],center = true);
    translate([65,0,35])rotate([0,32,0])cube([5,50,50],center = true);
}
}
//lianjiejian();
//称量料斗
module liaodou_chengliang(){
    $fn=50;
        difference(){
            minkowski(){
                M = [ [ 1  , 0  , 0.3  , 0   ],
                      [ 0  , 1  , 0, 0   ], 
                      [ 0  , 0  , 1  , 0   ],
                      [ 0  , 0  , 0  , 1   ] ] ;
            multmatrix(M) { 
               union() {
                    cylinder(r=10.0,h=10,center=false);
                   ld();
                } 
            }
          cylinder(r=40,h=1);
            }
            minkowski(){
                M = [ [ 1  , 0  , 0.3  , 0   ],
                      [ 0  , 1  , 0, 0   ], 
                      [ 0  , 0  , 1  , 0   ],
                      [ 0  , 0  , 0  , 1   ] ] ;
            multmatrix(M) {
                union() {
                   ld();
                } 
            }
       cylinder(r=38,h=1.5);   //出料口直径78
        }
    }
}
//liaodou_chengliang();
//气缸
module qigang(){
           union(){
     cylinder(r=8,h=150, center = true);
     translate([0,0,30])cylinder(r=15,h=120, center = true);
           }                    
}
//translate([-90,0,70])qigang();
//固定气缸系统
module gudingzuo(){
    translate([-60,0,28])rotate([0,-45,0])
         for (a = [-36:70:50])translate([0,a,0]){
             color("lime")cube([60,15,3],center = true);   
         } //固定转座  
     translate([-60,0,168])rotate([0,0,0])
         for (a = [-18:36:18])translate([-6,a,0]){
           color("lime")cube([40,15,3],center = true);   
         } //固定转座    
    {
     translate([-70,0,8]) rotate([90,0,0]) cylinder(r=4,h=100, center = true);
    translate([-90,0,168]) rotate([90,0,0]) cylinder(r=5,h=50, center = true);
     translate([-90,0,168]) rotate([90,0,0]) cylinder(r=8,h=15, center = true);
    color("lime")translate([-90,-16,168]) rotate([90,0,0]) cylinder(r=6,h=15,   center = true);
    color("lime")translate([-90,16,168]) rotate([90,0,0]) cylinder(r=6,h=15,    center = true);
    }
    {
     cylinder(r=50,h=2, center = true);
    translate([-70,0,0])cube([60,50,2], center = true);
   translate([-70,0,8]) rotate([90,0,0]) cylinder(r=4,h=100, center = true);
   translate([-70,0,8]) rotate([90,0,0]) cylinder(r=6,h=50, center = true);
    translate([-70,0,8]) rotate([90,0,0]) cylinder(r=6,h=50, center = true);
    color("lime")translate([-70,-36,8]) rotate([90,0,0]) cylinder(r=6,h=15,     center = true);
    color("lime")translate([-70,36,8]) rotate([90,0,0]) cylinder(r=6,h=15,      center = true);
    }
}
//gudingzuo();

//module text(){
 //color("cyan") {
////    translate([260,0,70])scale([3,3,3])rotate([90,0,0])text(str("chuanganqi"), halign = "center");
//    translate([-180,0,100])scale([3,3,3])rotate([90,0,0])text(str("qigang"), halign = "center");
//     translate([50,0,340])scale([3,3,3])rotate([90,0,0])text(str("liaodou,L：400，W:400，H：300，R30-40"), halign = "center");    
//translate([50,0,300])scale([3,3,3])rotate([90,0,0])text(str("chukouzhijing:60-80mm"), halign = "center");          
//       }  
// }    
 //传感器支架
               

//function ngon(num, r) = 
  //[for (i=[0:num-1], a=i*360/num) [ r*cos(a), r*sin(a) ]];

module loushuan(){
translate([0,0,0])
        for (a= [0:30:30])
            translate([0,0,a])
                 linear_extrude(height = 6, scale = 1) polygon(ngon(6, 6)) ;
        
translate([0,0,0])
    linear_extrude(height = 30, scale = 1)
         polygon(ngon(360, 3)) ;
}


//成品料斗
module liaodou_chengpin(){
color("white",0.5)
    translate([0, 0, 0])
        rotate_extrude($fn = 80)
            translate([78, 0])
                scale([7.5,7.5,7.5])
                     polygon( points=[[-5,-16],[-4.8,-16],[-0.2,0],[30.0,43.3],[30,58.3],[29.8,58.3],[29.8,43.3],[-0.2,0]]);
}
for (a = [0:620:620])
    translate([a,0,0])
        for (b = [0:620:620])
               translate([0,b,0]){    
                    liaodou_chengpin();
//                  translate([0,50,-150])rotate([0,0,45])shusongdai();
               }

//投料料斗
module ld_touliao(){
color("white",0.5)
    translate([0, 0, 0])
        rotate_extrude($fn = 80)
            translate([22.5, 0])
                     polygon( points=[[0,-211],[2,-211],[2,0],[75,65],[75,180+65],[73,180+65],[73,65],[0,0],[0,-211]]);   //料斗
    translate([0,0,-20])cube([130,50,10]);
}    

//称量料斗
module ld_chengliang(){
translate([225,300,-600]){
    translate([150,0,40])chuanganqi();
    loushuan();
    translate([205,0,-70])
    color("lime")cube([20,30,200],center = true);             
    lianjiejian();
    liaodou_chengliang(); 
     translate([-90,0,70])qigang(); 
     gudingzuo();  
}
}
// 输送带   
module shusongdai(){
    for (a = [-150:400:250])
        translate([a,0,0]){
            rotate([90,0,0]){
                 cylinder(r=20,h=150,center = true); 
                  color("white")
                       cylinder(r=8,h=200, center = true);
            }  
        }
    for (b = [0:35:35])  
        translate([-150,-75,15-b])
            cube([400,150,5]);     
}
for (a = [0:600:600])
    translate([a,0,-150])
        rotate([0,0,90])
            for (b = [0:600:600])
                translate([b,0,0])
                    shusongdai();
            
module moju(){
     translate([0, 0, 0])
        rotate_extrude($fn = 80){
            translate([140, 0])
              polygon( points=[[0,0],[-15,0],[-15,100],[0,100],[0,0]]);
           translate([70, 0])
             polygon( points=[[0,0],[-15,0],[-15,100],[0,100],[0,0]]);
    }     
}

//称量、投料、模具模块
for (a= [0:600:600])
    translate([-300+a,0,0]){
        ld_chengliang();           
    translate([200,300,-1440+211])
        ld_touliao();     
    translate([260,330,-1200])
        rotate([0,0,90])    
            scale([1,1,1.5])
               huatai_zong();
        for (a= [0:100:100])
               translate([110,300,-1640-a])
        moju();
}

module dimian(){
    color("lime",0.2)cube([1000,1000,0.01]);           
}  

translate([0,0,-2600]){dimian();translate([800,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("0.000"), halign = "center");}
translate([0,0,-1740]){dimian();translate([800,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("860"), halign = "center");}
translate([0,0,-1540]){dimian();translate([800,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("1060"), halign = "center");}        
translate([0,0,-1440]){dimian(); translate([800,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("1160"), halign = "center");}           
translate([0,0,-982]){dimian(); translate([800,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("1618"), halign = "center");}           
translate([0,0,0]){dimian(); translate([850,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("2600"), halign = "center");}            
translate([0,0,-120]){dimian(); translate([800,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("2480"), halign = "center");}           
translate([0,0,-180]){dimian(); translate([800,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("2420"), halign = "center");}            
translate([0,0,-300]){dimian(); translate([800,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("2300"), halign = "center");}            
translate([0,0,-600]){dimian(); translate([800,0,0])color("cyan")scale([6,6,6])rotate([90,0,0])text(str("2000"), halign = "center");}            

           
           




