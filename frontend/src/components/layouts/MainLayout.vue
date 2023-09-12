<template>
  <div>
    <Navbar />
    <slot></slot>

    <Footer />
  </div>
</template>

<script>
import Navbar from "../common/Navbar.vue";
import Footer from "../common/Footer.vue";

export default {
  name: "MainLayout",
  components: {
    Navbar,
    Footer,
  },
};
</script>
