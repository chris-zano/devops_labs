const nodemailer = require('nodemailer');
const fs = require('fs').promises;
const path = require('path');

const getSystemCredentials = () => {
    return {
        user: process.argv[2],
        pass: process.argv[3]
    }
}

const filepath = path.join(__dirname, '..', 'system_alert_email.json');

try {

    async function readFileData() {
        try {
            const data = await fs.readFile(filepath, 'utf-8');
            const jsonData = JSON.parse(data);

            const { subject, message } = jsonData;
            const { user, pass } = getSystemCredentials()

            const transporter = nodemailer.createTransport({
                service: "gmail",
                auth: { user, pass }
            });

            const options = {
                from: user,
                to: 'niico.ncs@gmail.com',
                subject: subject,
                html: `<p>${message}</p>`
            }

            transporter.sendMail(options)
                .then(response => {
                    console.log('node mailer sent message with a status of')
                })
                .catch(error => {
                    throw new Error(error);
                })
        } catch (err) {
            console.error('Error reading the file:', err);
        }
    }

    readFileData();

} catch (error) {
    console.error('an error occured:', error);
}
