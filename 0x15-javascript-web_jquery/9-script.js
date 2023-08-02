const hello = $('div#hello');
$.get('https://fourtonfish.com/hellosalut/?lang=fr', (response) => {
  hello.html(response.hello);
});
