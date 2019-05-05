$(function (){
	//轮播图
	var imgIndex = 0;
	var timer;
	function autoPlay(){
		//当前元素隐藏
		$("#banner img").eq(imgIndex).css("display","none");
		//更新下标
		imgIndex = ++imgIndex == $("#banner img").length ? 0 : imgIndex;
		//设置显示
		$("#banner img").eq(imgIndex).css("display","block");
	
	}
	//开启定时器
	timer = setInterval(autoPlay,2000);
	//鼠标移入移出
	$("#banner").mouseover(function (){
		clearInterval(timer);
	});
	$("#banner").mouseout(function (){
		timer = setInterval(autoPlay,2000);
	});
	$("#banner .prev").click(function (){
		//当前元素隐藏
		$("#banner img").eq(imgIndex).css("display","none");
		//更新下标
		imgIndex = --imgIndex == -1 ? $("#banner img").length-1 : imgIndex;
		//设置显示
		$("#banner img").eq(imgIndex).css("display","block");
	})
})
