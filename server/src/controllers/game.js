import {Router} from 'express';
import path from 'path';

let router = Router();

router.route('/')
	.get((req, res) => {
		res.sendFile(path.join(__dirname, "../views/game/main.html"));
	});

export default router;