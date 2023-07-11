<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { watch } from 'vue';

const { locale } = useI18n();

watch(locale, () => {
  localStorage.setItem('lang', locale.value);
});
</script>

<template>
  <select class="form-select" aria-label="Lang" v-model="locale">
    <option value="ru">RU</option>
    <option value="en">EN</option>
  </select>
</template>

<style scoped>
.form-select {
  width: 90px;
}
</style>
