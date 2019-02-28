//57步进电机
module motor57() {
    translate([0,0,90]){
        color("steelblue")translate([0,0,0])  
        rotate([0,0,0]) cylinder(56,28.5 ,28.5, center=true);
        color("Gray")translate([0,0,38])rotate([0,0,0])
        cylinder(20, 6, 6, center=true); 
    }
}

//57减速步进电机
module motor_s57() {
    translate([0,0,0]){
        color("Gray") rotate([0,0,0])
        cylinder(56,28.5 ,28.5, center=true);
        color("Gray")translate([0,0,70])rotate([0,0,0])
        cylinder(20, 6, 6, center=true); 
        color("Gray")translate([0,0,45.5])rotate([0,0,0])
        cylinder(35, 30, 30, center=true); 
    }   
}

//57减速电机支架
module motor_zhijia57() {
    translate([0,0,-36.5]){
        color("lime") translate([-35,0,-23])
        cube([2.5,57,46],true);
        color("lime") translate([0,0,0])
        cube([68,57,2.5],true);
    }
}
//42步进电机
module motor_42() {
    
    intersection() {
        color("steelblue") 
        translate([0,0,0])cube(42,42 ,40, center=true);
        translate([0,0,0])cylinder(42,25 ,25, center=true);
    }
    translate([0,0,20])cylinder(16,3 ,3, center=true);
    
}
//42电机支架
module motor_zhijia42(){
    translate([-3,0,-83]){
        color("lime") translate([-24,0,24])
        cube([2.5,48,48],true);
        color("lime") translate([0,0,0])
        cube([48,52,2.5],true);
    }
}    
//42电机平支架
module motor_zhijia42p(){
        color("lime") translate([0,0,0])
        cube([48,68,2.5],true);
}    


//42减速步进电机
module motor_s42() {
    translate([0,0,0]){
        color("Gray") rotate([0,0,0])
        cylinder(24,21 ,21, center=true);
        color("Gray")translate([0,0,22])rotate([0,0,0])
        cylinder(20, 22, 22, center=true); 
        color("Gray")translate([0,0,36])rotate([0,0,0])
        cylinder(18, 6, 6, center=true); 

    }   
}
//园底座
module dizuo_y(){
    translate([0,0,0]){
        difference() {
            color("Gray")translate([0,0,0])rotate([0,0,0])
            cylinder(210, 70, 70, center=true); 
            cylinder(210, 67, 67, center=true); 
            color("red")translate([0,0,0])rotate([0,0,0])
            cylinder(210, 67, 67, center=true); 
            color("SteelBlue") translate([-38,0,0])   
            cube([5,100,210],true);
            color("Gray")translate([0,0,-107])rotate([0,0,0])
            cylinder(3, 85, 85, center=true); 
            color("Gray")translate([0,0,107])rotate([0,0,0])
            cylinder(3, 85, 85, center=true); 
        }
    }
}

//园底座1
module dizuo_y1(){
    translate([0,0,0]){
        color("Gray")translate([0,0,0])rotate([0,0,0])
        cylinder(210, 70, 70, center=true); 
        color("red")translate([0,0,0])rotate([0,0,0])
        cylinder(210, 67, 67, center=true); 
        color("SteelBlue") translate([-38,0,0])   
        cube([5,100,210],true);
        color("Gray")translate([0,0,-107])rotate([0,0,0])
        cylinder(3, 85, 85, center=true); 
        color("Gray")translate([0,0,107])rotate([0,0,0])
        cylinder(3, 85, 85, center=true); 
        
    }
}

//底座


module dizuo(){
    translate([0,0,88]){
        difference() {
            color("SteelBlue") translate([1,0,80])
            cube([84,100,5],true);
            color("SteelBlue") translate([0,0,-145])
            cube([110,100,5],true);
            color("SteelBlue") translate([-38,0,-33])   
            cube([5,100,220],true);
            color("SteelBlue") translate([40,0,-33]) 
            cube([5,100,220],true);
        }
    }
}
//铜套轴承套
module gear_8(){  
    difference() {
        union(){
            color("lime") rotate([0,0,0])translate([0,0,15])
            cylinder(24,9,9, center=true);
            cylinder(6,15,15, center=true);
        }
        translate([0,0,12])
        cylinder(30,4,4, center=true);
    }        
}
//铜套轴承
module zc_huatao12(){
    color("lime") rotate([0,0,0])translate([0,0,28.5])
    cylinder(57,10.5,10.5, center=true);
    color("lime") rotate([0,0,0])translate([0,0,3])
    cylinder(6,21,21, center=true);
    color("red") rotate([0,0,0])
    hull(57,6 ,6, center=true); 
}
//铜套轴承
module zc_huatao8(){
    color("lime") rotate([0,0,0])translate([0,0,0])
    cylinder(24,7.5,7.5, center=true);
    color("lime") rotate([0,0,0])translate([0,0,-12])
    cylinder(4,16,16, center=true);
    color("red") rotate([0,0,0])
    hull(57,6 ,6, center=true); 
}

//密封过渡轴
module roller_l12(){
    color("Gray") translate([0,0,0])rotate([0,0,0])
    cylinder(180,6 ,6, center=true);
}
//卧式光杠固定座 12       
module gdz_os12(){
    translate([0,0,70]){
        color("Gray") rotate([0,0,0])translate([0,0,6])
        cylinder(12,16 ,16, center=true);
        color("Gray") rotate([0,0,0])translate([0,-18,6])
        cylinder(12,6,6, center=true);        
        color("Gray") rotate([0,0,0])translate([0,18,6])
        cylinder(12,6,6, center=true);  
    }
}
//卧式光杠固定座 8       
module gdz_os8(){
    translate([0,0,70]){
        difference() {
            color("Gray") rotate([0,0,0])translate([0,0,6])
            cylinder(10,15,15, center=true);
            cylinder(10,4,4, center=true); 
        }
         difference() {
            color("Gray") rotate([0,0,0])translate([0,-16,6])
            cylinder(10,6,6, center=true);
            cylinder(10,3,3, center=true);  
         }          
         difference() {
            color("Gray") rotate([0,0,0])translate([0,16,6])
            cylinder(10,6,6, center=true);
            cylinder(10,3,3, center=true);  
         }          
    }
}

//卧式光杠固定座 5       
module gdz_os5(){
    translate([0,0,70]){
        difference() {
            color("Gray") rotate([0,0,0])translate([0,0,6])
            cylinder(10,15,15, center=true);
            cylinder(10,2.5,2.5, center=true); 
        }
         difference() {
            color("Gray") rotate([0,0,0])translate([0,-16,6])
            cylinder(10,6,6, center=true);
            cylinder(10,3,3, center=true);  
         }          
         difference() {
            color("Gray") rotate([0,0,0])translate([0,16,6])
            cylinder(10,6,6, center=true);
            cylinder(10,3,3, center=true);  
         }          
    }
}

//立式光杠固定座        
module gdz_ls12(){
    translate([0,0,5]){
        color("Gray") rotate([0,0,0])translate([0,0,12]){
            translate([0,0,-12])cube([12,48,8],true);
            translate([0,0,0])cube([12,36,27],true);
        }        
        color("red") translate([0,0,10])rotate([0,90,0]){
        cylinder(12,6,6, center=true);  
        }
     }
}
//防水法兰
module fl_12(){
    color("red") translate([0,0,-6])rotate([0,0,0])
    cylinder(12,18,18, center=true);
}
//12联轴器
module lzq_12(){
    translate([0,0,0]){
        color("blue") rotate([0,0,0])translate([0,0,-17.5])
        cylinder(30,15,15, center=true);
    }
}

//12光杠
module guanggang_12(){
    translate([0,0,0]){
        color("steelblue") rotate([0,90,0])translate([0,0,6])
        cylinder(650,6,6, center=true);
    }
}
//光杠8
module guanggang_8(){
    translate([0,0,0]){
        color("steelblue") rotate([0,0,0])translate([0,0,0])
        cylinder(50,4,4, center=true);
    }
}
//滑动轴承12
module gear_12(){
    translate([0,0,0]){
        color("lime") rotate([0,0,0])translate([0,0,0])
        cube([36,40,35],true);
        color("red") translate([0,0,0])rotate([0,90,0])
        cylinder(36,6,6, center=true);
    }
}

//弹簧
module th(){
    translate([0,0,25]){
        r=5;
        for(g=[0:1:1889])
        color("yellow") rotate([0,0,0]) translate([0,0,0])
        translate([cos(g)*r,sin(g)*r,(g)/100])
        rotate(a=[80,0,g])
        cylinder(1.5,1.5,1.5,center=true,sin=3);
    }    
}

//丝杠
module sg(){
    translate([0,0,0]){
        r=4;
        for(g=[0:1:5889])
        color("yellow") rotate([0,0,0]) translate([0,0,0]) 
        translate([cos(g)*r,sin(g)*r,(g)/100])
        rotate(a=[80,0,g])
        cylinder(1.5,1.5,1.5,center=true,sin=3);
    }    
    translate([0,0,32]){
        color("yellow") rotate([0,0,0])
        cylinder(90,4,4,center=true,sin=3);
    }
}
//连接板
module ljb(){
    translate([50,0,-30]){
        intersection(){    
            color("yellow") translate([0,0,0])
            cube([5,80,80],true);
        }
        union(){
            color("yellow") 
            translate([40,0,-40]) cube([80,60,5],true);
            translate([-25,0,-5]) cube([50,40,5],true);
            translate([-25,0,-40]) cube([50,40,5],true);            
            
        }
    }  
}


//垂直部分

//工件
module gj_max(){
    color("steelBlue") translate([0,0,0]) 
    cube([40,40,15],true);
}
//工件_min
module gj_min(){
    color("Blue") translate([0,0,0]) 
    cube([20,10,10],true);
}
  //抓爪舵机
module dj(){
    color("Blue") translate([0,0,-15])  
    cube([56,56,25],true);
}

//左抓爪
module djz(){
    color("steelBlue") translate([0,0,-75])rotate([0,0,0])
    cube([10,60,110],true);
}

//螺母
module lm(){
    color("steelBlue") translate([0,0,0])   
    rotate([0,0,0])   
    cylinder(10,8,8, center=true);
}
//螺丝
module ls(){
    color("steelBlue") translate([0,0,0])   
    rotate([0,0,0])   
    cylinder(30,4,4, center=true);
    translate([0,0,20])  
    cube([14,14,8],true);
}


// 量取尺寸线
module ccx(){
    color("red") translate([0,0,0])   
    rotate([0,0,0])   
    cylinder(500,2,2, center=true);
}

//推力轴承12mm
module tlzc12(){
    difference(){  
        color("cyan") translate([0,0,0])rotate([0,0,0]) 
        cylinder(8,12,12, center=true);
        cylinder(8,6,6, center=true);
    }
}   
//驱动部件

module zdbj(){
    union(){
        translate([0,0,150])ccx();  //尺寸线
   //     translate([0,0,65])dizuo_y();  //支座
        motor_s57() ;   //57减速电机
        translate([0,0,100]) motor_zhijia57();   //减速电机支架        
        translate([0,0,100]) lzq_12();   //联轴器12
        translate([0,0,155])rotate([0,180,0]) zc_huatao12();  //轴承12    
        translate([0,0,165]) fl_12();      //防水法兰
        translate([0,0,150]) roller_l12();  //转轴
        translate([0,0,105]) gdz_os12();   //光轴固定座1
        translate([0,0,145]) gdz_os12();    //光轴固定座12  
        translate([0,0,170]) tlzc12();    //推力轴承12  
    }
}
//转动销轴
module zdxz(){
    translate([0,0,0]) {
        scale([1,1,0.5])translate([0,0,0]) roller_l12();  //转轴
        translate([0,0,0]) gdz_os12();   //光轴固定座1
        translate([0,0,]) gdz_os12();    //光轴固定座12  
        translate([0,0,75]) tlzc12();    //推力轴承12  
    }
}
//转动销轴1
module zdxz1(){
    translate([0,0,20]) {
        scale([1,1,0.3])translate([0,0,-20]) roller_l12();  //转轴
        rotate([0,0,0])translate([0,0,-75]) gear_8();   //滑动轴承
        translate([0,0,-75]) gdz_os12();    //光轴固定座12  
        translate([0,0,-15]) tlzc12();    //推力轴承12  
    }
}

//孔
module hole4(){
    cylinder(5,2,2, center=true);
}
//  滑套轴承8/15
module gear_8_15(){
    difference() {
        union() {
            color("lime") rotate([0,0,0])translate([0,0,0])
            cylinder(45,7.5,7.5, center=true);
            difference() {
                cylinder(5,16,16, center=true);
                rotate([0,0,0])translate([12.5,0,0])
                hole4();
                rotate([0,0,0])translate([-12.5,0,0])
                hole4();
                rotate([0,0,0])translate([0,12.5,0])
                hole4();
                rotate([0,0,0])translate([0,-12.5,0])
                hole4();
            }
        }
        translate([0,0,0])
        cylinder(45,4,4, center=true);
    }    
}   
//  滑套轴承8/15短
module gear_8_15_duan(){
    difference() {
        union() {
            color("lime") rotate([0,0,0])translate([0,0,0])
            cylinder(30,7.5,7.5, center=true);
            difference() {
                translate([0,0,-15])cylinder(5,16,16, center=true);
                rotate([0,0,0])translate([12.5,0,0])
                hole4();
                rotate([0,0,0])translate([-12.5,0,0])
                hole4();
                rotate([0,0,0])translate([0,12.5,0])
                hole4();
                rotate([0,0,0])translate([0,-12.5,0])
                hole4();
            }
        }
        translate([0,0,15])
        cylinder(30,4,4, center=true);
    }    
}   

//臂


//铝型材30303_1
module lxc3030_1(){
    color("blue") translate([0,0,0])rotate([0,0,0])
    cube([l1+50,30,30],true);
}

//铝型材30303_2
module lxc3030_2(){
    color("blue") translate([0,0,0])rotate([0,0,0])
    cube([l2+50,30,30],true);
}
    //铝型材30303_3
module lxc3030_3(){
    color("blue") translate([0,0,0])rotate([0,0,0])
    cube([l3+50,30,30],true);
}
    //铝型材30303_4
module lxc3030_4(){
    color("blue") translate([0,0,0])rotate([0,0,0])
    cube([l4+50,30,30],true);
}

//鏊子
module aozi(){
color("DarkViolet") translate([0,0,0])rotate([0,0,0])
 cylinder(260,200,200, center=true);
}

//翻转轴
module fanzhuanzhou(){
    union(){
        rotate([0,90,0]) {
            color("lime") rotate([0,0,0])translate([0,0,0])
               cylinder(500,4,4, center=true);
            color("blue")rotate([0,90,0])translate([0,0,0])
               cube([400,10,10], center=true);
        }
    }
}
//移动刀架
module yidongdaojia(){
    union(){
        rotate([0,0,0]) translate([0,0,12]){
            color("lime") rotate([0,0,0])translate([0,0,0])
               cube([80,12,12], center=true);                            
            rotate([0,90,0]) translate([0,0,-30])
                cylinder(6,15,15, center=true);
         }
    }      
}
//翻转刀
module fanzhuandao(){
    union(){
        rotate([0,0,0])translate([0,0,15]) {
            color("lime") rotate([0,0,0])translate([0,-210,-10])
               cube([40,450,0.5], center=true);                            
            rotate([0,90,0]) translate([0,0,0])
                cylinder(450,2,2, center=true);
        }
    }      
}
//组合翻转刀
module zuhefandao(){
    union(){
       translate([220,0,0])rotate([0,0,0])yidongdaojia();//左动刀架
       translate([220,0,0])rotate([0,0,0])fanzhuandao();//左下翻转刀
    }
}

//翻转部件
module fanzhuanbujian(){
    union(){
       translate([300,0,0])rotate([0,0,0])fanzhuanzhou();//翻转轴
       translate([-100,0,0])rotate([0,0,0])zuhefandao();//组合翻转刀
//       translate([-100,0,0])rotate([-45,0,0])zuhefandao();//组合翻转刀
       translate([250,0,0])rotate([-45,0,0])zuhefandao();//组合翻转刀
       translate([-90,0,0])rotate([0,90,0])motor57();//57电机
       translate([50,0,0])rotate([0,90,0])lzq_8();//联轴器
       translate([120,-0,-40])rotate([0,90,0])scale([1,1,5.5])sg();//丝杠
       translate([690,0,-40])rotate([0,-90,0])motor57();//57电机
       translate([550,0,-40])rotate([0,-90,0])lzq_8();//联轴器

    }
}



translate([0,250,30])rotate([0,0,0])fanzhuanbujian();
//折叠部件
module zhediebujian(){
   union(){
       translate([300,0,0])rotate([0,0,0])scale([0.5,1,1])fanzhuanzhou();//翻转轴
       translate([100,0,0])rotate([0,0,0])zuhefandao();//组合翻转刀
      translate([-40,0,0])rotate([0,90,0])motor57();//57电机
       translate([50,0,0])rotate([0,90,0])lzq_8();//联轴器
       translate([120,-0,-40])rotate([0,90,0])scale([1,1,0.5])scale([1,1,5.5])sg();//丝杠
       translate([520,0,-40])rotate([0,-90,0])motor57();//57电机
       translate([340,0,-40])rotate([0,-90,0])lzq_8();//联轴器
     }
}
//打蛋器
module dadanqi(){
       difference() {
           color("lime") 
                cube([155,325,295], center=true);                            
           rotate([0,0,0]) translate([0,80,0])
                cube([155,170,185], center=true);                            
    }
}
//容器
module rongqi(){
    color("blue")rotate([0,0,0]) translate([0,0,0])
        cylinder(150,80,90, center=true);
}
//打蛋部件
module dadanbujian(){
    translate([0,0,0])rotate([0,0,0]) dadanqi();
    translate([0,80-20])rotate([0,0,0]) rongqi();
}
rotate([0,0,90])translate([-150,-600,400])dadanbujian();

translate([0,350,-35])rotate([0,0,90])translate([-200,-600,400])scale([0.7,0.7,0.7])dadanbujian();

//工件抓取区域
module reg1(){
color("yellow") translate([0,0,0])rotate([0,0,0])
cube([220,40,1],true);
}

//底座
module dizuo(){
     color("lime") 
        cube([450,650,500], center=true); 
}  
translate([250,0,-480])dizuo();

//打蛋器支架
module zhijia_dadanqi(){
    color("blue") 
        cube([20,20,500], center=true); 
}
translate([500,0,0])zhijia_dadanqi()

//  "0“地面
{
//color("yellow") translate([0,0,-45]) 
//cylinder(1,720,700, center=true);
}



//        //旋转部分
  //支撑板
module zcb(){
    color("Blue") translate([0,-25,15])  
    cube([80,3,80],true);
    translate([0,-50,55])rotate([0,0,0])
    cube([45,50,3],true);
}

//抓爪(左）
module djzl(){
    union(){
        translate([0,0,-10]){
            color("Blue") translate([0,7.5,-25])rotate([0,0,0])
            cube([15,2,110],true);
            translate([7.5,0,-25])
            cube([2,15,110],true);
            translate([8.5,0,-85])rotate([0,0,0])
            cube([2,50,15],true);
        }
        
    }
}
//抓爪(右）
module djzr(){
    union(){
        translate([0,0,-10])rotate([0,0,0]){
            color("Blue") translate([0,7.5,-25])rotate([0,0,0])
            cube([15,2,110],true);
            translate([-7.5,0,-25])
            cube([2,15,110],true);
            translate([-8.5,0,-85])rotate([0,0,0])
            cube([2,50,15],true);
        }
        
    }
}
   //密封过渡轴
module roller_8(){
    color("Gray") translate([0,0,0])rotate([0,0,0])
    cylinder(200,4 ,4, center=true);
}
   //套筒
module roller_8_12(){
        difference() {
            color("steelblue") translate([0,0,0])rotate([0,0,0])
            cylinder(40,6 ,6, center=true);
            cylinder(40,4 ,4, center=true);
        }
}
//
  //ljb1连接板1
module ljb1(){
    color("Blue") translate([0,0,0])  
    cube([70,3,35],true);
}
  //ljg1连接杆1
module ljg1(){
    color("Blue") translate([0,0,0]) 
    cylinder(50,4,4, center=true);
}
//齿轮
module cl_50(){
    difference(){
        color("steelblue") rotate([0,0,0])translate([0,0,0])
        cylinder(15,25,25, center=true);
        cylinder(15,4,4, center=true);
        translate([16,0,0])cylinder(15,3,3, center=true);
        translate([-16,0,0])cylinder(15,3,3, center=true);
        translate([0,16,0])cylinder(15,3,3, center=true);
        translate([0,0-16,0])cylinder(15,3,3, center=true);         
        }
}
//小齿轮
module cl_20(){
    difference(){
        color("blue") rotate([0,0,0])translate([0,0,0])
        cylinder(15,10,10, center=true);
        translate([0,0,0])cylinder(15,4,4, center=true);
    }
}

//铜套轴承套
module gear_8(){  
    difference() {
        union(){
            color("lime") rotate([0,0,0])translate([0,0,15])
            cylinder(24,10,10, center=true);
            cylinder(6,15,15, center=true);
        }
        translate([0,0,12])
        cylinder(30,4,4, center=true);
    }        
}
    //齿条
module ct20(){
    color("blue") translate([0,0,0])rotate([0,0,0])
    cube([20,20,100],true);
}

//工作部件
module gzbj(){
    translate([0,55,8])rotate([0,0,0])zcb(); //支撑板  
    translate([0,0,70])rotate([0,0,0])roller_8_12();   //套筒
    translate([-25,15,0])rotate([0,90,90])cl_50();   //齿轮 
    translate([25,15,0])rotate([0,90,90])cl_50();   //齿轮  
    translate([25,15,35])rotate([0,90,90])cl_20();   //齿轮  
    translate([25,65,35])rotate([0,90,-90])motor_s42();//42减速步进电机
    translate([-25,0,0])rotate([0,0,0])djzl();   //舵机爪  
    translate([25,0,0])rotate([0,0,0])djzr();   //舵机爪        
    translate([25,30,0])rotate([0,90,90])gear_8();  //轴承
    translate([-25,30,0])rotate([0,90,90])gear_8();  //轴承
    translate([0,0,180])rotate([0,0,0])roller_8();   //光杆 
}
   
//旋转部件
module Rotate(){
   translate(0,0,0)rotate([0,0,0]){            
       { 
        translate([0,35,42])rotate([0,0,0])cl_50();   //齿轮  
        translate([0,0,43])rotate([0,0,0])cl_20();   //齿轮  
        translate([0,0,85])rotate([0,180,0])motor_s42();//42减速步进电机
        translate([0,15,52])rotate([0,0,0]) motor_zhijia42p();  //电机平支架
        translate([0,35,-45])rotate([0,0,0])gdz_os8();  //固定座 
        translate([0,35,45])gear_8_15_duan();  
        }
    }
}

//升降部件
module up_down(){
    translate([0,0,25]){
        translate([0,0,60])rotate([0,0,0])ct20();   //齿轮条
        translate([0,-15,0])rotate([0,0,0]){            
            translate([0,15,20])rotate([0,90,90])cl_20();   //齿轮  
            translate([0,65,15])rotate([0,90,-90])motor_s42();//42减速步进电机
            translate([0,58,65])rotate([0,0,90]) motor_zhijia42();  //电机支架
//            translate([0,0,0]) gdz_os12();    //光轴固定座12  
        }
    }
}
//translate([0,0,0])rotate([0,0,a2])up_down();




l0=275;
l1=230;
l2=230;
l3=l2;
l4=l1;
//计算A点：
p0=300;
//p0=sqrt(200*200+250*250);
B0=atan(0);

// 范围：B0/p0
// atan(250/200) >= B0 >= -atan(250/200)
// sqrt(700*700+200*200) >= p0 >= 200
// 
//p0=290/291：0度  转换点1 


//dian A:
g = (l1*l1-l0*l0/4+p0*p0-l2*l2)/(2*p0*cos(B0));
k = (l0+2*p0*sin(B0))/(2*p0*cos(B0));
a = k*k+1;
b = l0-2*g*k;
c = g*g+l0*l0/4-l1*l1;
ya = (-b-sqrt(b*b-4*a*c))/2/a;
xa = sqrt(l1*l1-(ya+l0/2)*(ya+l0/2));
yb = p0*sin(B0);
xb = p0*cos(B0);
a1 = atan((ya+l0/2)/xa);
//a1 = -180 -atan((ya+l0/2)/xa);
if (xb >= xa);
    a2=atan((p0*sin(B0)+l0/2-l1*sin(a1))/(p0*cos(B0)-l1*cos(a1)));

if (xb < xa);
 //  a2 = 180+atan((p0*sin(B0)+l0/2-l1*sin(a1))/(p0*cos(B0)-l1*cos(a1)));
    

// xa = 0 
// l1*l1-(ya-l0/2)*(ya-l0/2) = 0
// ya = l1 + l0/2
// a1 = 90

g1 = (l4*l4-l0*l0/4+p0*p0-l3*l3)/(2*p0*cos(B0));
k1 = (l0-2*p0*sin(B0))/(2*p0*cos(B0));
aa = 1+k1*k1;
b1 = 2*k1*g1-l0;
c1 = g1*g1+l0*l0/4-l4*l4;
yc = (-b1-sqrt(b1*b1-4*aa*c1))/2/aa;
xc = sqrt(l4*l4-(yc-l0/2)*(yc-l0/2));

// xc = 0 
// l4*l4-(yc-l0/2)*(yc-l0/2) = 0
// yc = l4 + l0/2
// a4 = 90

a4 = atan((yc-l0/2)/xc); 
//a4 = 180-atan((yc-l0/2)/xc); 
//p0*cos(B0)-l1*cos(a1) = 0
//a1 = acos(p0*cos(B0)/l1)

//   fangwei
a3 = -atan((l4*sin(a4)+l0/2-p0*sin(B0))/(p0*cos(B0)-l4*cos(a4)));
//a3 = 180-atan((l4*sin(a4)+l0/2-p0*sin(B0))/(p0*cos(B0)-l4*cos(a4)));



translate([-100,0,0]){
    color("cyan") {   

        translate([-100,-160,0])text(str("g= ", g), halign = "center");
        translate([0,-160,0])text(str("g1= ", g1), halign = "center");           
        translate([-100,-180,0])color("cyan") text(str("k = ", k), halign = "center");
        translate([0,-180,0]) color("cyan") text(str("k1 = ", k1), halign = "center");

        translate([-100,-200,0])text(str("a= ", a), halign = "center");
        translate([0,-200,0])text(str("aa= ", aa), halign = "center");

        translate([-100,-220,0]) color("cyan") text(str("b = ", b), halign = "center"); 
        translate([0,-220,0]) color("cyan") text(str("b1 = ", b1), halign = "center");
        translate([-100,-240,0])text(str("c= ", c), halign = "center");
        translate([0,-240,0])text(str("c1= ", c1), halign = "center");
               
        translate([-100,-120,0])text(str("p0= ", p0), halign = "center");
        translate([0,-120,0])text(str("B0= ", B0), halign = "center");


        translate([-100,-80,0])text(str("xa = ", xa), halign = "center");
    color("cyan") 
        translate([0,-80,0])text(str("ya = ", ya), halign = "center");
    color("cyan") 
        translate([-100,-60,0])text(str("xb = ", xb), halign = "center");
    color("cyan") 
        translate([0,-60,0])text(str("yb = ", yb), halign = "center");
    color("cyan") 
        translate([-100,-40,0])text(str("xc = ", xc), halign = "center");
    color("cyan") 
        translate([0,-40,0])text(str("yc = ", yc), halign = "center");
  
    color("cyan") 
        translate([-100,0,0])text(str("a1 = ", a1), halign = "center");
    color("cyan") 
        translate([0,0,0])text(str("a2 = ", a2), halign = "center");
    color("cyan") 
        translate([-100,-20,0])text(str("a3 = ", a3), halign = "center");
    color("cyan") 
        translate([0,-20,0])text(str("a4 = ", a4), halign = "center");
}
}    

h1=235;
h2=270;
h3=235;
h4=200;


//main:

translate([0,-l0/2,70])zdbj();   // 转动驱动部分1
translate([0,l0/2,0])zdbj();   // 转动驱动部分1     
translate([l1/2*cos(a1),l1/2*sin(a1)-l0/2,h1])rotate([0,0,a1])lxc3030_1();   //臂1
translate([l1*cos(a1)+l2/2*cos(a2),l1*sin(a1)+l2/2*sin(a2)-l0/2,h2])rotate([0,0,a2])lxc3030_2();   //臂2
translate([l4*cos(a4)+l3/2*cos(a3),l4*sin(a4)+l3/2*sin(a3)+l0/2,h3])rotate([0,0,a3])lxc3030_3();   //臂3
translate([l4/2*cos(a4),l4/2*sin(a4)+l0/2,h4])rotate([0,0,a4])lxc3030_4();   //臂4 
translate([l1*cos(a1),l1*sin(a1)-l0/2,h2])zdxz1();  //转动销轴
translate([l4*cos(a4),l4*sin(a4)+l0/2,h3])zdxz1();  //转动销轴
translate([0,0,50]){
    translate([p0*cos(B0),-35+p0*sin(B0),90])rotate([0,0,0])Rotate();   //转动部件

    translate([p0*cos(B0),p0*sin(B0),60])rotate([0,0,a])gzbj();   //工作部件     
    //translate([p0*cos(B0),p0*sin(B0),-40])rotate([0,0,25])gj_max();   //工件   
    translate([p0*cos(B0),p0*sin(B0),-40])rotate([0,0,a])gj_min();   //工件 
}
//translate([l1*cos(a1)+l2*cos(a2),l1*sin(a1)+l2*sin(a2),h2])rotate([0,0,90+a2])up_down();  //升降部件
translate([p0*cos(B0),p0*sin(B0),h2+10])rotate([0,0,180-a2])up_down();  //升降部件

translate([250,0,-100])rotate([0,0,0])aozi();  //鏊子
translate([200,-240,0])rotate([0,0,-30])reg1();  //工作抓取区域
translate([200,240,0])rotate([0,0,30])reg1();  //工作抓取区域




//防水法兰
module fl_8(){
    color("red") translate([0,0,0])rotate([0,0,0])
    cylinder(6,18,18, center=true);
}
//8联轴器
module lzq_8(){
    color("blue") translate([0,0,0])rotate([0,0,0])
    cylinder(30,15,15, center=true);
}

//8光杠
module guanggang_8_70(){
    color("steelblue") rotate([0,0,0])translate([0,0,0])
    cylinder(70,4,4, center=true);
}

//园底座
module dizuo_y8(){
    translate([0,0,0]){
        difference() {
            color("Gray")translate([0,0,0])rotate([0,0,0])
            cylinder(210, 70, 70, center=true); 
            cylinder(210, 67, 67, center=true); 
            color("red")translate([0,0,0])rotate([0,0,0])
            cylinder(210, 67, 67, center=true); 
            color("SteelBlue") translate([-38,0,0])   
            cube([5,100,210],true);
            color("Gray")translate([0,0,-107])rotate([0,0,0])
            cylinder(3, 85, 85, center=true); 
            color("Gray")translate([0,0,107])rotate([0,0,0])
            cylinder(3, 85, 85, center=true); 
        }
    }
}
//驱动部件

module zdbj_8(){
    union(){
        translate([0,0,150])ccx();  //尺寸线
   //     translate([0,0,65])dizuo_y8();  //支座
        motor_s42() ;   //42减速电机
        translate([0,0,-50]) rotate([0,180,180])motor_zhijia42();   //减速电机支架        
        translate([0,0,60]) lzq_8();   //联轴器12
        translate([0,0,100])rotate([0,0,0]) zc_huatao8();  //轴承12    
        translate([0,0,165]) fl_12();      //防水法兰
        translate([0,0,150]) roller_l12();  //转轴
        translate([0,0,105]) gdz_os12();   //光轴固定座1
        translate([0,0,145]) gdz_os12();    //光轴固定座12  
        translate([0,0,170]) tlzc12();    //推力轴承12  
    }
}

//��件区域圆
module yuan_wai(){
    cylinder(210, 70, 70, center=true); 
}
    

//translate([-300,0,0])zdbj_8();






