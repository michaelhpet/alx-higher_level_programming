#!/usr/bin/node
exports.esrever = function (list) {
  const length = list.length;
  return list.reduce((newList, element, i) => {
    newList[length - i - 1] = element;
    return newList;
  }, Array(length));
};
