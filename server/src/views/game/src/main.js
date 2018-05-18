
let resources = ["game/assets/images/treasureHunter.json"];
let g = hexi(512, 512, setup, resources, load);
g.backgroundColor = 0x5a96c6;
g.scaleToWindow();
g.start();

// 倒计时
let count = 60;
let second = 60;

// 出牌倒计时label
let timer = g.text("60", "36px puzzler", "white");
timer.visible = false;

function setup() {
	timer.x = g.canvas.width / 2 - timer.width / 2;
	timer.y = 20;

	g.state = play;
	timer.visible = true;
}

function load () {
	g.loadingBar();
}

function play() {
	// 倒计时
	second -= 1;
	if (second <= 0) {
		second = 60;
		count -= 1;
		timer.content = `${count}`;

		if (count <= 0) {
			// 发牌
			count = 60;
		}
	}
}