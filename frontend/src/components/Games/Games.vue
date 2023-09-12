<template>
  <div>
    <TitleDisplay title="Games" />

    <div class="bg-dark">
      <GameList />
      <hr />
      <div class="container d-flex justify-content-center">
        <router-link to="/add-game" class="btn btn-success mb-5">
          + Add Game
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import TitleDisplay from "../common/TitleDisplay.vue";
import GameList from "./GameList.vue";

export default {
  name: "Games",

  components: {
    GameList,
    TitleDisplay,
  },

  methods: {
    openModal() {
      this.isModalVisible = true;
      console.log(this.isModalVisible);
    },

    closeModal() {
      this.isModalVisible = false;
    },
  },
};
</script>
