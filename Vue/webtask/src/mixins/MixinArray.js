var myMixin = {
  data() {
    return {
      toCompare: []
    };
  },

  methods: {
    hello: function() {
      console.log("hello from mixin!");
    },
    passData(home, compare) {
      compare = home;
      console.log("hello from mixin!, passing data ...");
    }
  }
};

// // define a component that uses this mixin
// var Component = HomePage.extend({
//   toCompare : selected
// });

// var component = new Component(); // => "hello from mixin!"
