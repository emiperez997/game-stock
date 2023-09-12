import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "dashboard",
    component: () => import("./components/Dashboard/Dashboard.vue"),
  },
  {
    path: "/games",
    name: "games",
    component: () => import("./components/Games/Games.vue"),
  },
  {
    path: "/games/:id",
    name: "game",
    component: () => import("./components/Games/Game.vue"),
  },
  {
    path: "/add-game",
    name: "add-game",
    component: () => import("./components/Games/AddGame.vue"),
  },
  {
    path: "/edit-game/:id",
    name: "edit-game",
    component: () => import("./components/Games/EditGame.vue"),
  },
  {
    path: "/delete-game/:id",
    name: "delete-game",
    component: () => import("./components/Games/DeleteGame.vue"),
  },
  {
    path: "/companies",
    name: "companies",
    component: () => import("./components/Companies/Companies.vue"),
  },
  {
    path: "/company/:id",
    name: "company",
    component: () => import("./components/Companies/Company.vue"),
  },
  {
    path: "/add-company",
    name: "add-company",
    component: () => import("./components/Companies/AddCompany.vue"),
  },
  {
    path: "/consoles",
    name: "consoles",
    component: () => import("./components/Consoles/Consoles.vue"),
  },
  {
    path: "/genres",
    name: "genres",
    component: () => import("./components/Genre/GenreList.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
