import {Router} from 'express';

let router = Router();

router.route('/')
	.get((req, res) => {
		res.sendFile("main.html");
	});

export default router;