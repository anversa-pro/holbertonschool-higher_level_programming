$.get('https://fourtonfish.com/hellosalut/?lang=fr', (body, textStatus) => {
    if (textStatus === 'success') {
      $('#hello').text(body.hello);
    }
  });