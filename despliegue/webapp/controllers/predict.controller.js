const tf = require('@tensorflow/tfjs');
require('@tensorflow/tfjs-node');
var fs = require('fs');

exports.makePredictions = async (req, res, next) => {
    var model = await tf.loadLayersModel('file://resources/model.json');
    var x = new Float32Array(10);
    const inputData = tf.tensor2d([1.45, 0.0, 0.18, 0.45, 0.71, 5.0, 9.0, 4, 8.00, 3], [1, 10]);
    predict = model.predict(inputData);
    predict2 = await tf.argMax(predict, axis = 1).data()
    get_line('./resources/labels.txt', predict2["0"], function (err, line) {
        res.send({ "prediction": line.replace(/(\r\n|\n|\r)/gm, "") });
    })
};

function get_line(filename, line_no, callback) {
    var data = fs.readFileSync(filename, 'utf8');
    var lines = data.split("\n");

    if (+line_no > lines.length) {
        throw new Error('File end reached without finding line');
    }
    callback(null, lines[+line_no]);
}