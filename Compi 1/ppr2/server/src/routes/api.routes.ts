
import controller from '../controller/api.controller'
import express from 'express'
const router = express.Router();

router.get("/ping", controller.ping)


export default router;