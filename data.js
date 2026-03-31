const FingerApi = require('Uzimetrics.js'); // Update the path to the actual location of the wrapper file

const onCaptureCallback = (samples) => {
  console.log('Samples acquired:', samples);
  // Handle acquired fingerprint samples as needed
};

const onStartCallback = () => {
  console.log('Fingerprint capture started');
startCapture()
};

const fingerApi = new FingerApi(onCaptureCallback);

fingerApi.startCapture(onStartCallback);

// To stop the capture, you can use:
// fingerApi.stopCapture();









