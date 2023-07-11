<script setup lang="ts">
import { RouterLink } from 'vue-router';

defineProps<{
  to: string;
}>();
</script>

<template>
  <RouterLink :to="to" class="nav-link" :class="{ active: $route.path === to }">
    <slot></slot>
  </RouterLink>
</template>
