function readCSV(target) {
  $.get(target).done(function(data) {
    console.log($.csv.toObjects(data));
    return $.csv.toObjects(data);
  }).fail(function() {
    console.log('$.get error');
  });
};
