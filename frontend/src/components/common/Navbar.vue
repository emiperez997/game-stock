<template>
  <nav
    class="navbar navbar-expand-lg bg-dark text-light p-3"
    data-bs-theme="dark"
  >
    <div class="container">
      <a class="navbar-brand" href="/"> Play Pulse </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/" class="nav-link"> Home </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/games" class="nav-link"> Games </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/companies" class="nav-link">
              Companies
            </router-link>
          </li>
          <li>
            <router-link to="/genres" class="nav-link"> Genres </router-link>
          </li>
          <li>
            <router-link to="/consoles" class="nav-link">
              Consoles
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",

  data() {
    return {
      activeNav: "",
    };
  },

  mounted() {
    this.activeNav = this.$route.name;
    console.log(this.$route);
  },
};
</script>

<style></style>
