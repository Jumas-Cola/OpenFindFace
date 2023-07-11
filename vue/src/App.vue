<script setup lang="ts">
import NavLink from './components/nav/NavLink.vue';
import LangSelect from './components/LangSelect.vue';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();
</script>

<template>
  <div class="container d-flex mt-2">
    <div class="container">
      <header class="d-flex justify-content-center">
        <ul class="nav nav-pills">
          <li class="nav-item">
            <NavLink to="/">{{ t('search') }}</NavLink>
          </li>
          <li class="nav-item">
            <NavLink to="/upload">{{ t('upload') }}</NavLink>
          </li>
        </ul>
      </header>
    </div>

    <div>
      <LangSelect />
    </div>
  </div>

  <RouterView />
</template>
