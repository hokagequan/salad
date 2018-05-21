
let resources = ["game/assets/images/treasureHunter.json"];
let g = hexi(512, 512, setup, resources, load);
g.backgroundColor = 0x5a96c6;
g.scaleToWindow();
g.start();

// 倒计时
let count = 60;
let second = 60;

// 世界
let world = new World();

// 出牌倒计时label
let timer = g.text("60", "36px puzzler", "white");
timer.visible = false;

// 准备页面容器
let ready_group = g.group();


// Play btn
let play_btn = g.button();

// 准备
function make_ready_ui() {
	play_btn.x = g.stage.width / 2 - play_btn.width / 2;
	play_btn.y = g.stage.height / 2 - play_btn.height / 2;
	ready_group.addChild(play_btn);
}

function setup() {
	make_ready_ui()

	timer.x = g.canvas.width / 2 - timer.width / 2;
	timer.y = 20;

	world.setup();

	g.state = play;
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