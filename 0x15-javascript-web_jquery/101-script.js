$(function () {
  const myList = $("ul.my_list");
  const addItem = $("div#add_item");
  const removeItem = $("div#remove_item");
  const clearList = $("div#clear_list");

  addItem.click(() => {
    myList.append("<li>Item</li>");
  });

  removeItem.click(() => {
    lastItem = $("ul.my_list li:last-child")[0];
    if (lastItem) lastItem.remove();
  });

  clearList.click(() => {
    myList.html("");
  });
});
