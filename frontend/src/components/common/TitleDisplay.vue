<template>
  <h1 class="p-5 text-center">
    {{ title }}
  </h1>
</template>

<script>
export default {
  name: "TitleDisplay",

  props: {
    title: {
      type: String,
    },
  },
};
</script>

<style scoped>
h1 {
  font-size: 3rem;
  font-weight: 700;

  text-shadow: 0 0 10px hsla(0, 0%, 0%, 0.4);
}
</style>
