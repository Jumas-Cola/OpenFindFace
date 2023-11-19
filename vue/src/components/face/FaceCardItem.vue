<script setup lang="ts">
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const props = defineProps({
  faceData: {
    type: Object,
    required: true
  }
});

const getFaceDataProps = () => {
  return Object.keys(props.faceData).filter((key) => !['image', 'id'].includes(key));
};

const checkIsUrl = (url: string) => {
  if (!url) {
    return false;
  }
  return `${url}`.startsWith('http://') || `${url}`.startsWith('https://');
};
</script>

<template>
  <hr />
  <table class="table table-bordered">
    <tbody>
      <tr v-if="props.faceData.image">
        <th class="fw-bold" scope="row">{{ t('photo') }}</th>
        <td class="d-flex justify-content-end">
          <img :src="`/${props.faceData.image}`" width="100" height="100" />
        </td>
      </tr>
      <template v-for="key in getFaceDataProps()" :key="key">
        <tr>
          <th class="fw-bold" scope="row">{{ t(key) }}</th>
          <td class="text-end">
            <a v-if="checkIsUrl(props.faceData[key])" :href="props.faceData[key]" target="_blank">
              {{ props.faceData[key] }}
            </a>
            <span v-else>
              {{ props.faceData[key] }}
            </span>
          </td>
        </tr>
      </template>
    </tbody>
  </table>
</template>
