<template>
  <div>
    <TitleDisplay title="Companies" />
    <TopCompanies />
    <br />

    <div class="bg-dark">
      <CompaniesList />
      <hr />
      <div class="container">
        <router-link to="/add-company" class="btn btn-success mb-5">
          + Add Company
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import TitleDisplay from "../common/TitleDisplay.vue";
import TopCompanies from "./TopCompanies.vue";
import CompaniesList from "./CompaniesList.vue";

export default {
  name: "Companies",

  components: {
    TopCompanies,
    TitleDisplay,
    CompaniesList,
  },
};
</script>
