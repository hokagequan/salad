
let resources = [
	"game/assets/images/treasureHunter.json",
	"game/assets/images/btns.json"
	];
let g = hexi(1024, 512, setup, resources, load);
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

let bg, play_btn;

// let sp = g.sprite(btns["start_over.png"]);
// sp.vx = 0;

// 准备
function make_ready_ui() {
	// Background
	bg = g.sprite("bg.png");
	bg.width = g.canvas.width;
	bg.height = g.canvas.height;
	ready_group.addChild(bg);

	// Play btn
	play_btn = g.button([
		"start_nor.png",
		"start_over.png",
		"start_sel.png"
	]);
	play_btn.x = g.canvas.width / 2 - play_btn.width / 2;
	play_btn.y = g.canvas.height / 2 - play_btn.height / 2;
	play_btn.release = () => {
		console.log("I'm pressed!");
	};
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