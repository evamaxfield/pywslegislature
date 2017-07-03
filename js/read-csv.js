function readCSV(target) {
  $.get(target).done(function(data) {
    createCSVElements($.csv.toObjects(data));
  }).fail(function() {
    console.log('$.get error');
  });
};

function createCSVElements(data) {
  console.log('attempting to attach:', data);
  var headers = data[0];

  for (i = 0; i < data.length; i++) {
    $('#retrieved-data-container')
      .append(
        $('<div/>')
        .addClass('data-element transition-all-100')
        .attr('id', 'data-element-' + i)
      );
  }

  var dataElements = $('#retrieved-data-container').children();
  for (var i = 0; i < dataElements.length; i++) {
    var container = $(dataElements[i]);
    /*for (var j = 0; j < data[i].length; j++) {
      console.log(data[i]);
    }*/

    console.log(data[i]);
  }

};
