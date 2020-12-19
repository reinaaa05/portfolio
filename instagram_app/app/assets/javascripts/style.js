document.addEventListener("turbolinks:load"
, function () {
  $(function() {
  //slide//
    $('.picture').slick({
      dots: true,
      fade: true,
      arrows: true,
      prevArrow:'<div class="prev"></div>',
      nextArrow:'<div class="next"></div>',
    });

  //モーダル//
    $('.signup').click(function(){
      $('#signup-modal').fadeIn();
    });

    $('.login').click(function(){
      $('#login-modal').fadeIn();
    });

    $('.setting').click(function(){
      $('#setting-modal').fadeIn();
    });

    $('.close-modal').click(function() {
      $('#signup-modal').fadeOut();
      $('#login-modal').fadeOut();
      $('#setting-modal').fadeOut();
    });
    //コメント//
    $('.comment-show').click(function() {
      var $comennt = $(this).find('.comennt');
      if($comennt.hasClass('open')) {
        $comennt.removeClass('open');
        $comennt.slideUp();
        $(this).find('span').text('+');
        
      } else {
        $comennt.addClass('open'); 
        $comennt.slideDown();
        $(this).find('span').text('-');
      }
    });
  //article-body折りたたみ//
    var itemHeights = [];
  var returnHeight;
    $(".body-text").each(function(){ //ターゲット(縮めるアイテム)
      var thisHeight = $(this).height(); //ターゲットの高さを取得
      itemHeights.push(thisHeight); //それぞれの高さを配列に入れる
      $(this).addClass("is-hide"); //CSSで指定した高さにする
      returnHeight = $(this).height(); //is-hideの高さを取得
    });

  $(".readmore-btn").click(function(){ //トリガーをクリックしたら
    if(!$(this).hasClass("is-show")) {
      var index = $(this).index(".readmore-btn"); //トリガーが何個目か
      var addHeight = itemHeights[index]; //個数に対応する高さを取得
      $(this).addClass("is-show").next().animate({height: addHeight},200).removeClass("is-hide"); //高さを元に戻す
    } else {
      $(this).removeClass("is-show").next().animate({height: returnHeight},200).addClass("is-hide"); //高さを制限する
    }
  });
  });
})
