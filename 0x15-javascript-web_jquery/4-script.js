const toggleHeader = $('div#toggle_header');
toggleHeader.click(() => {
  const header = $('header');
  if (header.attr('class').includes('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.removeClass('green');
    header.addClass('red');
  }
});
