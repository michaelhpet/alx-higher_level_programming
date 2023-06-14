#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, element) => {
    return element === searchElement ? ++count : count;
  }, 0);
};
