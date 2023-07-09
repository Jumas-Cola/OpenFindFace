<script setup lang="ts">
import NavLink from './components/nav/NavLink.vue';
</script>

<template>
  <div class="container mt-2">
    <header class="d-flex justify-content-center">
      <ul class="nav nav-pills">
        <li class="nav-item">
          <NavLink to="/"> Поиск </NavLink>
        </li>
        <li class="nav-item">
          <NavLink to="/upload"> Загрузка </NavLink>
        </li>
      </ul>
    </header>
  </div>

  <RouterView />
</template>
