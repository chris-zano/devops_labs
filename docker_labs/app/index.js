
import express from 'express';
import bodyParser from 'body-parser';
import { fileURLToPath } from 'url';
import { createServer } from 'http';
import path, { dirname } from 'path';


const _filename = fileURLToPath(import.meta.url);
const __dirname = dirname(_filename);

const app = express();
const server = createServer(app);


const STATIC_FILES_PATH = path.join(__dirname, 'public');
const VIEW_ENGINE_PATH = path.join(__dirname, 'views');


app.use(bodyParser.json());
app.use(express.urlencoded({ extended: true }));
app.use('/public', express.static(STATIC_FILES_PATH));
app.set('views', VIEW_ENGINE_PATH);
app.set('view engine', 'ejs');

server.listen(3123, () => {
    console.log('App is live at http://localhost:3123')
});

app.get('/', (req, res) => {
    res.render('index')
})