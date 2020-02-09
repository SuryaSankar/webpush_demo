'use strict';

/* eslint-enable max-len */

self.addEventListener('install', function(event) {
  console.log('Service Worker installing.');
});

self.addEventListener('activate', function(event) {
  console.log('Service Worker activating.');
});

self.addEventListener('push', function(event) {
  console.log('[Service Worker] Push Received.');
  const pushData = event.data.text();
  console.log(`[Service Worker] Push received this data - "${pushData}"`);
  let data, title, body;
  try {
    data = JSON.parse(pushData);
    title = data.title;
    body = data.body;
  } catch(e) {
    title = "Untitled";
    body = pushData;
  }
  const options = {
    body: body
  };
  console.log(title, options);

  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});

// const applicationServerPublicKey = "BEPN_Vc8S-FsTiBAsOKe4zDNEdtsxIVHL96H4EMIAWHdCXh3b4BBqbYCGpy1j2pjmYOXclRRBdJDMRqD05j0mbk";

// function urlB64ToUint8Array(base64String) {
//   const padding = '='.repeat((4 - base64String.length % 4) % 4);
//   const base64 = (base64String + padding)
//     .replace(/\-/g, '+')
//     .replace(/_/g, '/');

//   const rawData = window.atob(base64);
//   const outputArray = new Uint8Array(rawData.length);

//   for (let i = 0; i < rawData.length; ++i) {
//     outputArray[i] = rawData.charCodeAt(i);
//   }
//   return outputArray;
// }


// self.addEventListener('notificationclick', function(event) {
//   console.log('[Service Worker] Notification click Received.');

//   event.notification.close();

//   event.waitUntil(
//     clients.openWindow('https://developers.google.com/web/')
//   );
// });

// self.addEventListener('pushsubscriptionchange', function(event) {
//   console.log('[Service Worker]: \'pushsubscriptionchange\' event fired.');
//   const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
//   event.waitUntil(
//     self.registration.pushManager.subscribe({
//       userVisibleOnly: true,
//       applicationServerKey: applicationServerKey
//     })
//     .then(function(newSubscription) {
//       // TODO: Send to application server
//       console.log('[Service Worker] New subscription: ', newSubscription);
//     })
//   );
// });
