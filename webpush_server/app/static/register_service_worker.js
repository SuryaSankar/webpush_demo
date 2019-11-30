'use strict';

function urlB64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4);
  const base64 = (base64String + padding)
    .replace(/\-/g, '+')
    .replace(/_/g, '/');

  const rawData = window.atob(base64);
  const outputArray = new Uint8Array(rawData.length);

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }
  return outputArray;
}

function updateSubscriptionOnServer(subscription, apiEndpoint) {
  // TODO: Send subscription to application server

  return fetch(apiEndpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      subscription_json: JSON.stringify(subscription)
    })
  });

}

function subscribeUser(swRegistration, applicationServerPublicKey, apiEndpoint) {
  const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
  swRegistration.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: applicationServerKey
  })
  .then(function(subscription) {
    console.log('User is subscribed.');

    return updateSubscriptionOnServer(subscription, apiEndpoint);

  })
  .then(function(response) {
    if (!response.ok) {
      throw new Error('Bad status code from server.');
    }
    return response.json();
  })
  .then(function(responseData) {
    console.log(responseData);
    if (responseData.status!=="success") {
      throw new Error('Bad response from server.');
    }
  })
  .catch(function(err) {
    console.log('Failed to subscribe the user: ', err);
    console.log(err.stack);
  });
}

function registerServiceWorker(serviceWorkerUrl, applicationServerPublicKey, apiEndpoint){
  let swRegistration = null;
  if ('serviceWorker' in navigator && 'PushManager' in window) {
    console.log('Service Worker and Push is supported');

    navigator.serviceWorker.register(serviceWorkerUrl)
    .then(function(swReg) {
      console.log('Service Worker is registered', swReg);
      subscribeUser(swReg, applicationServerPublicKey, apiEndpoint);

      swRegistration = swReg;
    })
    .catch(function(error) {
      console.error('Service Worker Error', error);
    });
  } else {
    console.warn('Push messaging is not supported');
  } 
  return swRegistration;
}