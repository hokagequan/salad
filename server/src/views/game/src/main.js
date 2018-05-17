
let resources = ["game/assets/images/treasureHunter.json"];
let g = hexi(512, 512, setup, resources, load);
g.backgroundColor = 0x000000;
g.scaleToWindow();
g.start();

function setup() {
	
	g.state = play;
}

function load () {
	g.loadingBar();
}

function play() {

}