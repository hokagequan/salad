
let resources = ["game/assets/images/treasureHunter.json"];
let g = hexi(512, 512, setup, resources, load);
g.backgroundColor = 0x5a96c6;
g.scaleToWindow();
g.start();

// 出牌倒计时label
let timer = g.text("60", "36px puzzler", "white");
timer.visible = true;

function setup() {
	timer.x = g.stage.width / 2;
	timer.y = 30
	// timer.poistion.set(g.stage.width / 2, 30);

	g.state = play;
}

function load () {
	g.loadingBar();
}

function play() {

}