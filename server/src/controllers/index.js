import express from 'express';
import game from './game' 

let router = express.Router();

router.use('/', game);

export default router;