var c=["red","yellow","green","orange","purple","brown"];
var c1=["color of blood","hug diya be","grass looks like","you can eat it too!","red+blue","chetan ki jhant"];
var a=document.getElementsByClassName("square");
var inc=0;
var pickedColor=c[inc];
var r=document.querySelector(".reset");
var ques=document.querySelector(".ques");
for(var i=0;i<a.length;i++){
	a[i].style.background=c[i];

	a[i].addEventListener("click",function(){
		var clickedcolor=this.style.backgroundColor;
		console.log(clickedcolor);
		if(pickedColor==clickedcolor){
			for(var i=0;i<a.length;i++){
			a[i].style.background=clickedcolor;


			}
		}else{
			this.style.background="#232323";
		}
	
		if(pickedColor==clickedcolor){
			window.alert("BINGO");
		
		if(inc==(c.length-1)){
			inc=0;
		}
		
	}
		
		
	});
}

var r=document.querySelector(".reset");

r.addEventListener("click",back);
r.addEventListener("click",function(){
	r.style.background="#232323";
	r.style.color="white";
})
function back(){
	for(var i=0;i<a.length;i++){
	a[i].style.background=c[i];

	
}		
		if(inc==(c.length-1)){
			inc=0;
		}
		inc++;
		ques.innerHTML=c1[inc];
		pickedColor=c[inc];

}
/*
squares.style.background="yellow";
console.log(c[1])
for(var i=0;i<c.length;i++){
	squares[i].style.background=c[i];
}*/