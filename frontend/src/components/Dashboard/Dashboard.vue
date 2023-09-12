<template>
  <div>
    <TitleDisplay title="Dashboard" />
    <div class="bg-dark text-center">
      <GameList :limit="4" order="desc" order-by="year" title="Recent Games" />
      <!-- See more -->
      <div class="p-5">
        <router-link to="/games" class="btn btn-primary">
          See All Games
        </router-link>
      </div>
    </div>
    <br />
    <div class="bg-dark text-center">
      <TopCompanies />
      <div class="p-5">
        <router-link to="/companies" class="btn btn-primary">
          See All Companies
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import GameList from "../Games/GameList.vue";
import TitleDisplay from "../common/TitleDisplay.vue";
import TopCompanies from "../Companies/TopCompanies.vue";

export default {
  name: "Dashboard",

  components: {
    GameList,
    TopCompanies,
    TitleDisplay,
  },
};
</script>
