const addItem = $("div#add_item");
addItem.click(() => {
  const list = $("ul.my_list");
  list.append("<li>Item</li>");
});
