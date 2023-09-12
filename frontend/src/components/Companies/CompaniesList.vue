<template>
  <div class="bg-dark p-5">
    <div class="container">
      <h3 class="text-light text-center list-title">
        {{ title }}
      </h3>

      <div class="table-responsive text-center" v-if="companies.length">
        <table class="table table-dark table-hover text-center">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Name</th>
              <th scope="col">Foundation Year</th>
              <th scope="col">Country</th>
              <th scope="col">Games in Play Pulse</th>
              <th scope="col">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(value, key) in companies" :key="value.company_id">
              <th scope="row">{{ key + 1 }}</th>
              <td>{{ value.name }}</td>
              <td>{{ value.foundation_year }}</td>
              <td>{{ value.country }}</td>
              <td>{{ value.games.length }}</td>
              <td>
                <router-link :to="value.link" class="btn btn-primary m-2">
                  <i class="bi bi-box-arrow-up-right"></i>
                </router-link>

                <router-link :to="value.link" class="btn btn-success m-2">
                  <i class="bi bi-pencil-square"></i>
                </router-link>

                <router-link :to="value.link" class="btn btn-danger m-2">
                  <i class="bi bi-trash"></i>
                </router-link>
              </td>
            </tr>
          </tbody>
        </table>
        <!-- <nav aria-label="..." class="d-flex justify-content-center">
          <ul class="pagination bg-dark text-light">
            <li class="page-item" :class="hasPrevious ? '' : 'disabled'">
              <a class="page-link"> Previous </a>
            </li>
            <li class="page-item" v-for="page in pages">
              <a
                class="page-link"
                href="#"
                :class="page == actualPage ? 'active' : ''"
              >
                {{ page }}</a
              >
            </li>

            <li class="page-item" :class="hasNext ? '' : 'disabled'">
              <a class="page-link" href="/"> Next </a>
            </li>
          </ul>
        </nav> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CompaniesList",
  props: {
    title: {
      type: String,
      default: "All Companies",
    },
    limit: {
      type: Number,
      default: 0,
    },
    orderBy: {
      type: String,
      default: "name",
    },
    order: {
      type: String,
      default: "asc",
    },
    offset: {
      type: Number,
      default: 0,
    },
  },

  data() {
    return {
      companies: [],
      hasNext: false,
      hasPrevious: false,
      pages: 0,
      actualPage: 1,
    };
  },

  methods: {
    getCompanies() {
      axios
        .get(
          `http://localhost:5000/api/company?limit=${this.limit}&offset=${this.offset}&order_by=${this.orderBy}&order=${this.order}`
        )
        .then((response) => {
          this.companies = response.data.data;

          this.companies.map((company) => {
            company.link = `/company/${company.company_id}`;
          });

          this.hasNext = response.data.has_next;
          this.hasPrevious = response.data.has_previous;
          this.pages = response.data.total_pages;
          this.actualPage = response.data.page;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.getCompanies();
  },
};
</script>
