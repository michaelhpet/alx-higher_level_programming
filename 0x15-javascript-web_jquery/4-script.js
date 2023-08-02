const redHeader = $("div#toggle_header");
redHeader.click(() => {
  const header = $("header");
  if (header.attr("class").includes("red")) {
    header.removeClass("red");
    header.addClass("green");
  } else {
    header.removeClass("green");
    header.addClass("red");
  }
});
