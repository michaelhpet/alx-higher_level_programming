const redHeader = $('div#red_header');
redHeader.click(() => {
  $('header').css({
    color: '#FF0000'
  });
});
