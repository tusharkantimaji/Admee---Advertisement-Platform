var count_1 = 0;
document.getElementById("like").innerText(count_1);

function i_like(User_id_to) {
  couunt_1 = count_1 + 1;
}
function i_like() {
  $.ajax({
    url: "like_python_file.py",
    context: document.body,
  }).done(function () {
    alert("You Liked");
  });
}
